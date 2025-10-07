#!/usr/bin/env python3
"""
Test script for Bearer token authentication
"""

import requests
import time
import subprocess
import signal
import sys

# Test configuration
HOST = "127.0.0.1"
PORT = 8001
TOKEN = "test-secret-token-123"
ENDPOINT = f"http://{HOST}:{PORT}/mcp"


def test_authentication():
    """Test Bearer token authentication"""
    print("=" * 60)
    print("Testing Bearer Token Authentication")
    print("=" * 60)

    # Test 1: Request without Authorization header
    print("\n1. Testing request WITHOUT Authorization header...")
    try:
        response = requests.post(ENDPOINT, json={
            "jsonrpc": "2.0",
            "method": "tools/list",
            "params": {},
            "id": 1
        }, timeout=5)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        if response.status_code == 401:
            print("   ✓ PASS: Correctly rejected request without auth")
        else:
            print("   ✗ FAIL: Should have returned 401")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")

    # Test 2: Request with invalid token format
    print("\n2. Testing request with INVALID token format...")
    try:
        response = requests.post(ENDPOINT,
            json={
                "jsonrpc": "2.0",
                "method": "tools/list",
                "params": {},
                "id": 2
            },
            headers={"Authorization": "InvalidFormat token123"},
            timeout=5
        )
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        if response.status_code == 401:
            print("   ✓ PASS: Correctly rejected invalid format")
        else:
            print("   ✗ FAIL: Should have returned 401")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")

    # Test 3: Request with wrong token
    print("\n3. Testing request with WRONG token...")
    try:
        response = requests.post(ENDPOINT,
            json={
                "jsonrpc": "2.0",
                "method": "tools/list",
                "params": {},
                "id": 3
            },
            headers={"Authorization": "Bearer wrong-token"},
            timeout=5
        )
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        if response.status_code == 403:
            print("   ✓ PASS: Correctly rejected wrong token")
        else:
            print("   ✗ FAIL: Should have returned 403")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")

    # Test 4: Request with correct token
    print("\n4. Testing request with CORRECT token...")
    try:
        response = requests.post(ENDPOINT,
            json={
                "jsonrpc": "2.0",
                "method": "tools/list",
                "params": {},
                "id": 4
            },
            headers={"Authorization": f"Bearer {TOKEN}"},
            timeout=5
        )
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print("   ✓ PASS: Request accepted with valid token")
            result = response.json()
            if "result" in result and "tools" in result["result"]:
                print(f"   ✓ Found {len(result['result']['tools'])} tools")
        else:
            print(f"   ✗ FAIL: Should have returned 200, got {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")

    # Test 5: CORS preflight (OPTIONS)
    print("\n5. Testing CORS preflight (OPTIONS)...")
    try:
        response = requests.options(ENDPOINT, timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code in [200, 204]:
            print("   ✓ PASS: OPTIONS request allowed without auth (CORS preflight)")
        else:
            print(f"   Note: Got status {response.status_code}")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")

    print("\n" + "=" * 60)
    print("Authentication tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    print("\nStarting server with authentication...")
    print(f"Command: python server.py --file README.md --transport streamable-http --port {PORT} --auth-token {TOKEN}")
    print("\nPlease start the server manually in another terminal with:")
    print(f"  python server.py --file README.md --transport streamable-http --port {PORT} --auth-token {TOKEN}")
    print("\nWaiting for server to be ready...")

    # Wait for user to start server
    input("\nPress Enter when the server is running...")

    # Run tests
    test_authentication()
