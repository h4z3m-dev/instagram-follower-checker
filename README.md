# instagram-follower-checker
# Follower Comparison Tool: Find Who Doesn’t Follow Back

## Description
This script extracts and compares follower and following data from JSON files to identify users who do not follow back. It is useful for analyzing non-mutual connections on social media accounts.

## Features
- Extracts usernames from JSON files.
- Compares the list of following vs. followers.
- Identifies users who do not follow back.
- Outputs the list of non-mutual followers to a text file.

## Requirements
- Python 3.x

## Usage
1. Place your `following.json` and `followers_1.json` files in the script directory.
2. Run the script using:
   ```bash
   python script.py
   ```
3. The script will generate two extracted text files:
   - `following after extracting.txt`
   - `followers after extracting.txt`
4. A final output file, `Who Doesn’t Follow Back.txt`, will contain the list of users who don’t follow back.

## Installation
Clone the repository:
```bash
git clone https://github.com/h4z3m-dev/instagram-follower-checker.git
```
Navigate to the project directory:
```bash
cd instagram-follower-checker
```
Run the script:
```bash
python script.py
```

## Contributing
Feel free to contribute by submitting issues or pull requests!

## License
This project is licensed under the MIT License.

---
Let me know if you need modifications! 🚀

