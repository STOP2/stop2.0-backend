FAILED=0

if ! curl -X GET http://localhost:5000/stops?lat=60.20583\&lon=24.96293 | grep -q '"stop_name": "A.I. Virtasen aukio"'; then
  echo "Integration test 1 failed!"
  FAILED=1
fi


if [ $FAILED -eq 0 ]; then
  echo "Integration tests passed!"
  exit 0
else
  echo "Integration tests failed!"
  exit 1
fi
