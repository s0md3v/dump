### Generate this on your own

#### Grabbing results
Run the following query in [Google BigQuery](https://console.cloud.google.com/bigquery) and save the results
```sql
WITH
  deep AS(
  WITH
    nested AS(
    SELECT
      configurations.nodes AS arr
    FROM
      `red-team-project.bq_nvd.nvd`
    WHERE
      EXISTS (
      SELECT
        nodes.children
      FROM
        UNNEST(configurations.nodes) AS nodes
      WHERE
        EXISTS (
        SELECT
          cpe_match.cpe23Uri
        FROM
          UNNEST(nodes.cpe_match) AS cpe_match
        WHERE
          cpe_match.vulnerable = TRUE)) )
  SELECT
    a.cpe_match AS one
  FROM
    nested
  CROSS JOIN
    UNNEST(arr) a )
SELECT
  b.cpe23Uri
FROM
  deep
CROSS JOIN
  UNNEST(one) AS b
```
#### Parsing

> Note: Remove the first line from the file which contains "two" i.e. column name

The dump can now be parsed to the given format by the following Python program
```python
import re

cpes = set()

with open('cve.txt', 'r') as file:
	for line in file:
		line = re.match(r'(^(?:[^:]+:){6})', line.rstrip('\n')).group(1)
		line = line.replace('cpe:2.3:', 'cpe:/').rstrip(':')
		cpes.add(line)

cpes = sorted(cpes)

with open('cve.txt', 'w') as file:
    for cpe in cpes:
        file.write('%s\n' % cpe)
```
