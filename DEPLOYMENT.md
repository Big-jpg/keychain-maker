# 🚀 Deployment Guide

This guide explains how to deploy the OpenSCAD Keychain Maker application.

## 📦 Local Deployment

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Git

### Setup Steps

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/keychain-maker.git
cd keychain-maker
```

2. **Create a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the application:**

```bash
streamlit run app.py
```

Or use the provided script:

```bash
./run.sh
```

The app will be available at `http://localhost:8501`

## 🌐 Cloud Deployment Options

### Option 1: Streamlit Community Cloud (Recommended)

**Free hosting for Streamlit apps!**

1. **Push your code to GitHub:**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/keychain-maker.git
git push -u origin main
```

2. **Deploy to Streamlit Cloud:**

- Go to [share.streamlit.io](https://share.streamlit.io)
- Sign in with GitHub
- Click "New app"
- Select your repository: `yourusername/keychain-maker`
- Set main file path: `app.py`
- Click "Deploy"

3. **Configure (if needed):**

- Streamlit Cloud will automatically detect `requirements.txt`
- For OpenSCAD support, you'll need to add system dependencies (see below)

**Note:** OpenSCAD CLI rendering may not work on Streamlit Cloud without custom configuration. Users can still generate `.scad` files and render them locally.

### Option 2: Docker Deployment

1. **Create a Dockerfile:**

```dockerfile
FROM python:3.11-slim

# Install OpenSCAD
RUN apt-get update && apt-get install -y \
    openscad \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. **Build and run:**

```bash
docker build -t keychain-maker .
docker run -p 8501:8501 keychain-maker
```

### Option 3: Heroku

1. **Create `Procfile`:**

```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. **Create `setup.sh`:**

```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. **Deploy:**

```bash
heroku create your-app-name
git push heroku main
```

### Option 4: AWS EC2 / DigitalOcean / VPS

1. **SSH into your server**

2. **Install dependencies:**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv openscad -y
```

3. **Clone and setup:**

```bash
git clone https://github.com/yourusername/keychain-maker.git
cd keychain-maker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Run with systemd (persistent service):**

Create `/etc/systemd/system/keychain-maker.service`:

```ini
[Unit]
Description=OpenSCAD Keychain Maker
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/keychain-maker
Environment="PATH=/home/ubuntu/keychain-maker/venv/bin"
ExecStart=/home/ubuntu/keychain-maker/venv/bin/streamlit run app.py --server.port=8501 --server.address=0.0.0.0

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable keychain-maker
sudo systemctl start keychain-maker
```

5. **Setup reverse proxy with Nginx (optional):**

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## 🔧 Configuration

### Environment Variables

You can configure the app using environment variables:

```bash
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Streamlit Configuration

Create `.streamlit/config.toml`:

```toml
[server]
port = 8501
address = "0.0.0.0"
headless = true

[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

## 📝 Notes

- **OpenSCAD Requirement:** Full STL rendering requires OpenSCAD CLI to be installed on the deployment server
- **Without OpenSCAD:** The app will still work for generating `.scad` files, but STL rendering will be disabled
- **File Storage:** Generated files are temporary and stored in memory/temp directories
- **Scaling:** For high traffic, consider using a load balancer and multiple instances

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Find and kill the process using port 8501
lsof -ti:8501 | xargs kill -9
```

### Permission Denied

```bash
# Make sure scripts are executable
chmod +x run.sh
```

### OpenSCAD Not Found

```bash
# Install OpenSCAD
sudo apt install openscad  # Ubuntu/Debian
brew install openscad      # macOS
```

## 🔒 Security Considerations

- Use HTTPS in production (Let's Encrypt with Certbot)
- Set up firewall rules to restrict access
- Consider authentication for sensitive deployments
- Regularly update dependencies for security patches

## 📊 Monitoring

Consider adding monitoring tools:

- **Uptime monitoring:** UptimeRobot, Pingdom
- **Application monitoring:** New Relic, Datadog
- **Logs:** Papertrail, Loggly

---

For more information, see the main [README.md](README.md)
