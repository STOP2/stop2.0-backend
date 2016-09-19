if curl -X GET http://localhost:5000 | grep -q 'Hello World!'; then
  echo "Integration tests passed!"
  exit 0
else
  echo "Integration tests failed!"
  exit 1
fi
