mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml

echo "\
[theme]\n\
primaryColor = \"#f08080\"\n\
backgroundColor = \"#ffd6a5\"\n\
secondaryBackgroundColor = \"#ffffff\"\n\
textColor = \"#000000\"\n\
font = \"sans serif\"\n\
" > ~/.streamlit/config.toml