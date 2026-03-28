import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 1. This is where Django will look for your source static files
STATIC_URL = 'static/'

# 2. This is the "filesystem path" the error is asking for.
# It tells Django to gather all static files into a folder named 'staticfiles' in your root directory.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 3. (Optional but recommended) If you have a custom static folder in your root
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]