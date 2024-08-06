#!/usr/bin/env python3

import base64
import sys

def obfuscate_token(token):
    # 将 token 转换为字节
    token_bytes = token.encode('utf-8')
    # 使用 Base64 编码
    obfuscated_bytes = base64.b64encode(token_bytes)
    # 转换为字符串
    obfuscated_token = obfuscated_bytes.decode('utf-8')
    return obfuscated_token

def deobfuscate_token(obfuscated_token):
    # 将混淆后的 token 转换为字节
    obfuscated_bytes = obfuscated_token.encode('utf-8')
    # 使用 Base64 解码
    token_bytes = base64.b64decode(obfuscated_bytes)
    # 转换为字符串
    token = token_bytes.decode('utf-8')
    return token

def save_token_to_file(token, filename):
    with open(filename, 'w') as file:
        file.write(token)

def read_token_from_file(filename):
    with open(filename, 'r') as file:
        token = file.read().strip()
    return token

def main():
    if len(sys.argv) < 2:
        print("Usage: python token_manager.py <action> [token] [--file <filename>]")
        print("\tpython token_manager.py obfuscate <token>")
        print("\tpython token_manager.py deobfuscate [--file <filename>]")
        sys.exit(1)

    action = sys.argv[1]
    if action == 'obfuscate':
        if len(sys.argv) != 3:
            print("Error, \tpython token_manager.py obfuscate <token>")
            sys.exit(1)
        token = sys.argv[2]
        obfuscated_token = obfuscate_token(token)
        save_token_to_file(obfuscated_token, filename)
        print(f"Token obfuscated and saved to {filename}")
    elif action == 'deobfuscate':
        filename = 'token'
        if len(sys.argv) > 2 and sys.argv[3] == '--file' and len(sys.argv) > 3:
            filename = sys.argv[3]
        obfuscated_token = read_token_from_file(filename)
        token = deobfuscate_token(obfuscated_token)
        print(f"Original token: {token}")
    else:
        print("Invalid action. Use 'obfuscate' or 'deobfuscate'.")


if __name__ == '__main__':
    main()
