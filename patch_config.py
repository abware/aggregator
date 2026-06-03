import yaml
import sys

def patch_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if 'proxies' not in data or not data['proxies']:
        print("No proxies found, skipping patch.")
        return

    # 提取所有节点名
    proxy_names = [p['name'] for p in data['proxies']]

    # 补全 proxy-groups
    data['proxy-groups'] = [{
        'name': '🚀 手动选择',
        'type': 'select',
        'proxies': proxy_names + ['DIRECT']
    }]

    # 补全 rules
    data['rules'] = ['MATCH,🚀 手动选择']

    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

if __name__ == '__main__':
    patch_yaml(sys.argv[1])
