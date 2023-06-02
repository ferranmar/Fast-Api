## Comandos importantes
```python
pip install "fastapi[all]"
uvicorn main:app --reload
```


## FAQ

**Q: Por que se especifica async delante de las funciones?**

**A:** Que algo sea síncrono significa que si nosotros llamamos desde el movil al servidor y nuestra aplicacion no puede haceer absolutamente nada hasta que retorne algo el servidor... Esto seria un caos pero a veces seria necesario *e.g: Entrar a la pagina web*

**Q: Como puedo ver las funciones que realiza la Aplicacion?**

**A_** Añadiendo /docs en la url puedes ver todo el tipo de funciones. Tambien puedes utilizar /redoc