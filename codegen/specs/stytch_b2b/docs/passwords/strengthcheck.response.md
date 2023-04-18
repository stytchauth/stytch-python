- `breach_detection_on_create`: Will return true if breach detection will be evaluated. By default this option is enabled. This option can be disabled by contacting support@stytch.com. If this value is false then breached_password will always be false as well.

- `breached_password`: Returns true if the password has been breached. Powered by [HaveIBeenPwned](https://haveibeenpwned.com/).

- `luds_feedback`: Feedback for how to improve the password's strength using [luds](https://stytch.com/docs/docs/passwords#strength-requirements)

- `score`: The score of the password determined by [zxcvbn](https://stytch.com/docs/docs/passwords#strength-requirements). Values will be between 1 and 4, a 3 or greater is required to pass validation.

- `strength_policy`: The strength policy type enforced, either zxcvbn or luds.

- `valid_password`: Returns true if the password passes our password validation. We offer two validation options, zxcvbn is the default option which offers a high level of sophistication. We also offer LUDS. If an email address is included in the call we also require that the password hasn't been compromised using built-in breach detection powered by HaveIBeenPwned.

- `zxcvbn_feedback`: Feedback for how to improve the password's strength using [zxcvbn](https://stytch.com/docs/docs/passwords#strength-requirements).
