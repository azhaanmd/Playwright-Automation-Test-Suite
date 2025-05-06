# 1️⃣ Start with an official Python image
FROM python:3.11-slim

# Explanation:
# This creates a lightweight virtual computer (container) with Python 3.11 installed.
# 'slim' means it's smaller/faster.

# 2️⃣ Set the working directory inside the container
WORKDIR /app

# Explanation:
# This is like saying: "When you're inside the container, act like you're inside the /app folder."

# 3️⃣ Copy your project files into the container
COPY . .

# Explanation:
# This copies everything from your project folder (on your PC) into the container's /app folder.

# 4️⃣ Install system packages (needed by browsers and Playwright)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxss1 \
    libasound2 \
    libxshmfence1 \
    libgbm-dev \
    libdrm2 \
    libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Explanation:
# Playwright browser drivers (like Chromium) need some system libraries to run.

# 5️⃣ Install Python packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Explanation:
# Installs all the Python dependencies your project needs (from requirements.txt).

# 6️⃣ Install Playwright Browsers
RUN playwright install --with-deps

# Explanation:
# Installs the actual browsers (Chromium, Firefox, WebKit) and their system dependencies.

# 7️⃣ Set environment variable to avoid playwright sandbox issues
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Explanation:
# Ensures that Playwright installs browsers in the correct path inside Docker.

# 8️⃣ Default command to run tests
CMD ["pytest", "-v"]

# Explanation:
# This is the default thing the container will do when it runs: run your test suite with verbose output.
