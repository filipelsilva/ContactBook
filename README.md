# ContactBook (version 0.6)

A program to manage your contacts, written in Python3, made by Filipe Ligeiro Silva

## Usage

```text
python3 contact_book.py [-h] [-v | -a | -r | -e | -l | -la] [-n] [-p] [-m]
```

### Modes

```text
-h, --help: help about the program
-v, --verbose: verbose mode (all help will be displayed in the program, go use it! WARNING: in verbose mode, you can discard changes on exit. In command mode, that is not possible)
-a, --add: adds a contact to the book (requires name, phone number, email)
-r, --remove: removes a contact from the book (requires the name of the contact)
-e, --edit: edits a contact (requires the name of the contact)
-l, --list: lists a contact (requires the name of the contact)
-la, --listall: lists all contacts
```

### Variables

```text
-n, --name: name of the contact
-p, --phone: phone number of the contact
-m, --email: email of the contact
```

## Usage examples (command mode only)

### Adding a contact

```bash
python3 contact_book.py -a -n <name> -p <number> -m <email>
```

### Removing a contact

```bash
python3 contact_book.py -r -n <name>
```

### Editing a contact

```bash
python3 contact_book.py -e -n <name>
```

### Listing a contact

```bash
python3 contact_book.py -l -n <name>
```

### Listing all contacts

```bash
python3 contact_book.py -la
```

## To-do list

- Maybe change the argparse
