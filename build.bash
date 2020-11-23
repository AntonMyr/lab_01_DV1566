if docker build -t testapp . && docker run -dp 5000:5000 -t testapp; then
	echo success
else
	echo failed
fi
