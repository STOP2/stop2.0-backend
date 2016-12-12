#!/usr/bin/env bash

FAILED=0

# DigitransitAPIService tests

# returns correct stop
if ! curl -X GET http://localhost:5000/stops?lat=60.20583\&lon=24.96293 | grep -q '"stop_name": "A.I. Virtasen aukio"'; then
  echo 'Integration test "returns correct stop" failed'
  FAILED=$((FAILED+1))
fi

# returns correct number of stops if one stop
if [ ! `curl -X GET http://localhost:5000/stops?lat=60.203978\&lon=24.9633573 | grep -o '"stop":' | wc -l` -eq 1 ]; then
  echo 'Integration test "returns correct number of stops if one stop" failed'
  FAILED=$((FAILED+1))
fi

# returns correct number of stops if many stops
if ! [ `curl -X GET http://localhost:5000/stops?lat=60.1701305\&lon=24.9380825 | grep -o '"stop":' | wc -l` -eq 3 ]; then
  echo 'Integration test "returns correct number of stops if many stops" failed'
  FAILED=$((FAILED+1))
fi

# returns at least one bus_id
#commented out for now because the test is time sensitive => test will fail at nighttime. some mocking or a stop with 24h traffic needed to make this usable)
#if ! curl -X GET http://localhost:5000/stops?lat=60.203978\&lon=24.9633573 | grep -q '"trip_id":'; then
#  echo 'Integration test "returns at least one vehicle_id" failed'
#  FAILED=$((FAILED+1))
#fi

# returns correct numbers of bus_ids
if ! [ `curl -X GET http://localhost:5000/stops?lat=60.203978\&lon=24.9633573 | grep -o '"trip_id":' | wc -l` -le 10 ]; then
  echo 'Integration test "returns correct number of vehicle_ids" failed'
  FAILED=$((FAILED+1))
fi

# returns an empty array of stops if there are no stops nearby
if curl -X GET http://localhost:5000/stops?lat=60.2106153\&lon=25.0308546 | grep -q '"stop":'; then
  echo 'Integration test "returns an empty array of stops if there are no stops nearby" failed'
  FAILED=$((FAILED+1))
fi

# returns an empty array of stops if lat and long are incorrect
if ! curl -X GET http://localhost:5000/stops?lat=-1\&lon=12.5 | grep -q '"stops":' && curl -X GET http://localhost:5000/stops?lat=-1\&lon=12.5 | grep -q -v '"stop":'; then
  echo 'Integration test "returns an empty array of stops if lat and long are incorrect" failed'
  FAILED=$((FAILED+1))
fi


if [ $FAILED -eq 0 ]; then
  echo "Integration tests passed!"
  exit 0
else
  echo "$FAILED Integration tests failed!"
  exit 1
fi
