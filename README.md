# Credit Card Generator

This is a simple Credit Card Generator written in Python. The generator can produce credit card numbers for different card providers. Please note that this tool is intended for educational and testing purposes only. **Do not use it for illegal activities**.

## How to Change Card Provider

To change the card provider for the generated credit card numbers, you can modify the configuration in the `config.py` file. The available card providers are:

- **mastercard**
- **visa**
- **visa13**
- **visa16**
- **visa19**
- **amex**
- **diners**
- **discover**
- **jcb**
- **jcb15**
- **jcb16**
- **maestro**

Simply open the `config.py` file and change the value of the `card_provider` variable to your desired card provider. (default is mastercard)

```python
class config():
    # Only put the provider from the option given below

    # mastercard
    # visa
    # visa13
    # visa16
    # visa19
    # amex
    # diners
    # discover
    # jcb
    # jcb15
    # jcb16
    # maestro

    card_provider = "mastercard"
    
config = config()
```

Remember, generating credit card numbers for real financial transactions is illegal and unethical. This tool is meant for educational purposes and to validate software systems that accept credit card numbers.

Please use this tool responsibly and only in accordance with the law. The author of this repository is not responsible for any misuse or illegal activities carried out using this tool.
