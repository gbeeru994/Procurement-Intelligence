#!/usr/bin/env python3
"""
API Documentation Generator
Generates OpenAPI/Swagger documentation for the Procurement Intelligence API
"""

import json
from api.main import app

def generate_api_docs():
    """Generate API documentation"""
    print("Generating API documentation...")

    # Get OpenAPI schema
    openapi_schema = app.openapi()

    # Save as JSON
    with open("api-docs.json", "w") as f:
        json.dump(openapi_schema, f, indent=2)

    # Generate HTML documentation
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Procurement Intelligence API Documentation</title>
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.7.2/swagger-ui.css" />
    <style>
        html {{
            box-sizing: border-box;
            overflow: -moz-scrollbars-vertical;
            overflow-y: scroll;
        }}
        *, *:before, *:after {{
            box-sizing: inherit;
        }}
        body {{
            margin:0;
            background: #fafafa;
        }}
    </style>
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist@5.7.2/swagger-ui-bundle.js"></script>
    <script src="https://unpkg.com/swagger-ui-dist@5.7.2/swagger-ui-standalone-preset.js"></script>
    <script>
        window.onload = function() {{
            const ui = SwaggerUIBundle({{
                url: 'api-docs.json',
                dom_id: '#swagger-ui',
                deepLinking: true,
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIStandalonePreset
                ],
                plugins: [
                    SwaggerUIBundle.plugins.DownloadUrl
                ],
                layout: "StandaloneLayout"
            }});
        }};
    </script>
</body>
</html>
"""

    with open("api-docs.html", "w") as f:
        f.write(html_content)

    print("✅ API documentation generated:")
    print("  - api-docs.json (OpenAPI schema)")
    print("  - api-docs.html (Interactive documentation)")

    # Print summary
    paths = openapi_schema.get("paths", {})
    print(f"\n📊 API Summary:")
    print(f"  - Total endpoints: {len(paths)}")
    print(f"  - API version: {openapi_schema.get('info', {}).get('version', 'N/A')}")
    print(f"  - Title: {openapi_schema.get('info', {}).get('title', 'N/A')}")

    # Count endpoints by method
    method_counts = {}
    for path, methods in paths.items():
        for method in methods.keys():
            method_counts[method.upper()] = method_counts.get(method.upper(), 0) + 1

    print("  - Endpoints by method:")
    for method, count in method_counts.items():
        print(f"    {method}: {count}")

if __name__ == "__main__":
    generate_api_docs()