`wl` is a command line utility for converting strings to a given casing style.

![demo](https://i.ibb.co/MfywFxQ/Screenshot-2021-03-13-20-40-06.png)

### Usage
```
Usage of wl:
  -c string
        casing style (required)
  -i string
        input file (default stdin)
  -o string
        output file (default stdout)
```

### Supported styles

> Note: You don't need to use the words `foo` and `bar`, any word e.g. `prod_api_id` will work. `wl` will detect the casing style of your word and apply it to your wordlist. This can be handy in cases like changing your wordlist according to the input recieved from another tool.

#### Popular
`foobar, foo_bar, fooBar, FooBar, FOOBAR, FOO_BAR`

#### Cusom
`foo-bar, FOO-BAR, foo.bar, FOO.BAR, Foo.Bar, Foo_Bar, Foo-Bar, foo.Bar, foo.Bar, foo_Bar, foo-Bar`
