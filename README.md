# Shifter Github Actions

[![getshifter/actions-base](http://dockeri.co/image/getshifter/actions-base)](https://hub.docker.com/r/getshifter/actions-base/)

- [getshifter/actions-start](https://github.com/marketplace/actions/start-shifter-wordpress)
- [getshifter/actions-stop](https://github.com/marketplace/actions/stop-shifter-wordpress)

## Start Shifter WordPress action

Start Shifter's WordPress and store WordPress URL in the outputs `shifter_app_url`.
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

## Stop Shifter WordPress action

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
      uses: getshifter/actions-start@v2
      env:
        SHIFTER_USER: ${{ secrets.SHIFTER_USER }}
        SHIFTER_PASS: ${{ secrets.SHIFTER_PASS }}
        SHIFTER_SITE_ID: ${{ secrets.SHIFTER_SITE_ID }}
    - name: Show WordPress URL
      env:
        SHIFTER_APP_URL: ${{ steps.start.outputs.shifter_app_url }}
      run:
        echo ${SHIFTER_APP_URL}
    - name: Stop WordPress
      uses: getshifter/actions-stop@v2
      env:
        SHIFTER_USER: ${{ secrets.SHIFTER_USER }}
        SHIFTER_PASS: ${{ secrets.SHIFTER_PASS }}
        SHIFTER_SITE_ID: ${{ secrets.SHIFTER_SITE_ID }}
```

- (optional)`SHIFTER_APP_KEEP`: Use when do not want to stop the container.
  - It is set automatically if the container has already been started when executing `actions/start`.
