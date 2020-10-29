from win10toast import ToastNotifier

# this is a just simple example of the use of win10toast,
# but think of all the ways this can be included in scripts!


# the module's repo https://github.com/jithurjacob/Windows-10-Toast-Notifications

toaster = ToastNotifier()

toaster.show_toast("Hello there!", # title
                    "Basic-Python-Scripts", # body text
                    icon_path="custom.ico", # notifications can have an icon (by default has a python icon).
                    duration=5) # notifications can have set durations.
