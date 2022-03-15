<h2 align="center">
    Don't Panic
</h2>

### Contributions are welcome !

1. [Fork it](https://github.com/tudstlennkozh/dontpanic/fork)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

### You want to add your language to the AddIn ?

Great :thumbsup: ! 

1. No coding skills required !
2. Please follow the steps above ... **just use the following for branch name** : i8n/\<language> where you will put your language instead of \<language>
3. here are some guidelines to know where to change things in order to translate _dontpanic_.
   - `description/description_xx.txt` will store the translated description of AddIn 
     (`xx` is language code)
   - `description.xml` includes :
     - `<display-name>` : title for AddIn
     - `<extension-description>` : relative path to `description/description_xx.txt`
   - `CalcAddin.xcu` includes :
     - `DisplayName` : name of the function in your locale
     - `Description` : translation of the function's role
     - `Parameters` : translated name for `string` type
4. Please note that [LibreOffice seems](https://wiki.documentfoundation.org/LibreOffice_Localization_Guide/Adding_a_New_Language_or_Locale#Overview) to use the [ISO 639](https://en.wikipedia.org/wiki/ISO_639-1) language code