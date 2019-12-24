# Shifter Github Actions

- getshifter/actions/start
- getshifter/actions/stop






## Start Sfhiter WordPress action

Start Shifter's WordPress and store the base64-encoded WordPress URL in the environment variable `SHIFTER_APP_URL`.
If WordPress is already running, get the URL.

### Inputs / Outputs

None

### environment variable for other jobs

- `SHIFTER_APP_URL`: Base64 encoded WordPress URL.
- `SHIFTER_APP_KEEP`: Used to skip stop if WordPress is already running at the time of job execution. default The default value is `false`(string).

## Stop Sfhiter WordPress action

Stop WordPress of Shifter.

### Inputs / Outputs

None

## Example usage

```
uses: getshifter/actions/stop@master
env:
  SHIFTER_USER: ${{ secrets.SHIFTER_USER }}
  SHIFTER_PASS: ${{ secrets.SHIFTER_PASS }}
  SHIFTER_SITE_ID: ${{ secrets.SHIFTER_PASS }}
```

- (optional)`SHIFTER_APP_KEEP`: Use when do not want to stop the container.
  - It is set automatically if the container has already been started when executing `actions/start`.
