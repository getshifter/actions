# Shifter Github Actions

- getshifter/actions/start
- getshifter/actions/stop

## Start Sfhiter WordPress action

Start Shifter's WordPress and store WordPress URL in the outputs `SHIFTER_APP_URL`.
If WordPress is already running, get the URL.

### Requirements environment variable

- `SHIFTER_USER`: Login username for Shfter
- `SHIFTER_PASS`: Password
- `SHIFTER_SITE_ID`: Site ID to launch WordPress

### Inputs

None

### Outputs

- `shifter_app_url`: WordPress Live URL.

### set environment variable for other jobs

- `SHIFTER_APP_KEEP`: Used to skip stop if WordPress is already running at the time of job execution. default The default value is `false`(string).

## Stop Sfhiter WordPress action

Stop WordPress of Shifter.

### Requirements environment variable

- `SHIFTER_USER`: Login username for Shfter
- `SHIFTER_PASS`: Password
- `SHIFTER_SITE_ID`: Site ID to Stop WordPress

### Inputs / Outputs

None

## Example usage

```
    steps:
    - uses: actions/checkout@v1
    - name: Start WordPress
      id: start
      uses: getshifter/actions/start@master
      env:
        SHIFTER_USER: ${{ secrets.SHIFTER_USER }}
        SHIFTER_PASS: ${{ secrets.SHIFTER_PASS }}
        SHIFTER_SITE_ID: ${{ secrets.SHIFTER_SITE_ID }}
    - name: Show WordPress URL
      run:
        echo ${{ steps.start.outputs.shifter_app_url }}
    - name: Stop WordPress
      uses: getshifter/actions/stop@master
      env:
        SHIFTER_USER: ${{ secrets.SHIFTER_USER }}
        SHIFTER_PASS: ${{ secrets.SHIFTER_PASS }}
        SHIFTER_SITE_ID: ${{ secrets.SHIFTER_SITE_ID }}
```

- (optional)`SHIFTER_APP_KEEP`: Use when do not want to stop the container.
  - It is set automatically if the container has already been started when executing `actions/start`.
