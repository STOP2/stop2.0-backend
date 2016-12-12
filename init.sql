CREATE TABLE request (
	id serial,
	trip_id text,
	stop_id text,
	user_id text,
	device_id text,
	req_time timestamp with time zone,
	canceled boolean,
	cancel_time timestamp with time zone,
	pushed boolean
);

CREATE TABLE report (
  id serial,
  trip_id text,
  stop_id text,
  user_id text,
  report_time timestamp with time zone
);

CREATE TABLE vehicle (
  id serial,
  vehicle_id text,
  trip_id text
);