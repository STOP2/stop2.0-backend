CREATE TABLE request (
	id serial,
	trip_id text,
	stop_id text,
	user_id text,
	device_id text,
	req_time timestamp with time zone,
	canceled boolean,
	cancel_time timestamp with time zone
);

CREATE TABLE report (
  id serial,
  trip_id text,
  stop_id text,
  user_id text,
  report_time timestamp with time zone
);
