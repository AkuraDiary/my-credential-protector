# my-credential-protector 🥙
[ Type ] : Personal Project
[ Description ] :
A simple project to make simple things such as securing credentials to be complicated af, implementing my cipher project that [you can found it here](https://github.com/AkuraDiary/sigma_ciphers_cryptograms) and some hashing stuff


## My Backround creating this project 🍞

I used to save my credentials in ```.txt``` file and scatter it all around my folders. so i want to make some kinda of folder where i can safely put my credentials in it. And i'd like it to be accessed locally. So i learned about how to validating a file, some ciphers, and made this project to wrapped it all. After all, why not

## Would you like to try it? 🥘

> step 1 clone this repos into your local machine (make sure you have git installed)
```
git clone https://github.com/AkuraDiary/my-credential-protector.git
```

> step 2 Navigate and open the terminal in directory you cloned this project to then type
```
py mcp.py
```

> place your credentials files in ```.\credentials``` directory in ```.txt``` format, and the program will automatically detected it

> ### ENJOY 🍻

## TODO LIST OF THIS PROJECT 🥞
- Add safe update and backup mechanism
- Match the cli and gui mode features
- Add more crucial features like edit the file on the go
- Add Documentation

## PREVIEW
> ### This Project has 2 mode, CLI and GUI mode (on the way to match the feature on both mode)

### CLI MODE
<details>
  <summary>Menus</summary>
  
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/climode.png)
  
</details>

<details>
  <summary>Scan Secured Credentials</summary>
  
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/climode1.png)
  
</details>

<details>
  <summary>Read Secured Credentials</summary>
  
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/climode2.png)
  
</details>

<details>
  <summary>Scan New Credentials</summary>
  
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/climode3_empty.png)
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/climode3_found.png)
  
</details>
<details>
  <summary>Update</summary>
  
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/climode4.png)
  
</details>

### GUI MODE
<details>
  <summary>Menus</summary>
  
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/uimode.png)
  
</details>

<details>
  <summary>Add New Credentials</summary>
  
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/uimode_add.png)
  
</details>

<details>
  <summary>Read Secured Credentials</summary>
  
  ![Previews](https://github.com/AkuraDiary/my-credential-protector/blob/main/images/uimode_open.png)
  
</details>

## How it basically works? 🥯
```
- First it will generate token and private key for you (you'll be prompted to set the token length tho)
- Then it will ask you to create a credential (username and master password)
- It will secure it by saving the hashed credential and not the credential itself
- After that, put all of your credentials that you saved in `.txt` files into ```.\credentials``` dir
- And it will scan the dir and automatically encrypted all of your `.txt` files 
- It will save it into ```.\secured-credentials``` directory and clear the ```.\credentials``` dir
- If you want to read the file, you just need to choosed it from the app

All of the process here is happened locally, you only need internet connection when you first run it 
(to clone the dependencies it needed)
```
## NOTE 🥖
```
### Developed in python 3.10 and only using built in libraries 🥛
### Works on Windows, because i don't have mac or linux machine to tested it💀
```

## Contributing 🍪
### if you'd like to contribute into this project, i would be so happy, check how to contribute [here](https://github.com/AkuraDiary/my-credential-protector/blob/main/CONTIBUTING.md)
