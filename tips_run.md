### veiw nohup log (nohup.out)
- tail -f nohup.out => show last 10 lines realtime
- tail -f nohup.out | grep "key word" => show the lines including key word realtime
- tail -n -10 nohup.out => show last 10 lines at once
- tail -n +10 nohup.out => show after 10 lines at once

### stop process
- jobs
- kill %1

### kill process by grep
- ps -ef | grep username | grep .py
- kill -9 \`ps -ef|grep username | grep .py|awk '{print $2}'\`
