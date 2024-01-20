# PNG to ICO Converter

## Readme
1. [Readme: Italiano](./README_IT.md)
2. [Readme: English](./README.md)

## Descrizione
Questo programma è un convertitore da PNG a ICO. Consente di selezionare un file PNG e convertirlo in un file ICO. L'ICO è un formato di file utilizzato per le icone nei sistemi operativi Windows.

## Dipendenze
- PyQt5
- pillow

## Utilizzo
1. Installa le dipendenze necessarie:
```
pip install PyQt5
pip install pillow
```

2. Esegui il programma:
```
python converter.pyw
```

3. Nella finestra principale del programma, clicca sul pulsante "Converti da PNG a ICO".

4. Verrà visualizzata una finestra di dialogo per selezionare un file PNG da convertire. Seleziona il file desiderato e clicca su "Apri".

5. Verrà effettuato un controllo per verificare se il file selezionato è effettivamente un file PNG. Se non lo è, verrà visualizzato un messaggio di errore.

6. Successivamente, verrà visualizzata una finestra di dialogo per selezionare il percorso di salvataggio per il file ICO convertito. Seleziona il percorso desiderato e clicca su "Salva".

7. Il file PNG verrà convertito in un file ICO e verrà visualizzato un messaggio di conferma con il percorso di salvataggio del file ICO.

## Compilazione programma

1. Installa le dipendenze necessarie:
```
pip install pyinstaller
```

2. Una volta installato PyInstaller, puoi utilizzarlo per creare un eseguibile dallo script Python. Ecco un esempio di comando per creare un eseguibile su Windows:

```shell
pyinstaller --onefile --windowed --icon=img/logo.ico --name=PNGtoICO --version-file=version_info.txt converter.pyw
```

## Eseguibile

Nella cartella `build` troverai il file `PNGtoICO.zip`, che contiene la versione eseguibile dello script `converter.pyw`. 

## Screenshot

![Screenshot PNGtoICO](img/screenshot.png)