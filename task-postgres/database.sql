CREATE INDEX IF NOT EXISTS short_names_name_index ON short_names (name);
CREATE INDEX IF NOT EXISTS full_names_name_index ON full_names (name);
UPDATE full_names
SET status = sn.status
FROM short_names sn
WHERE split_part(full_names.name, '.', 1) = sn.name;