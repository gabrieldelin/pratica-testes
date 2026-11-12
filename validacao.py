# teste
def email_valido(email):
  if not email:
    return False
  if "@" not in email:
    return False
  usuario, dominio = email.split("@",1)
  return usuario != "" and "." in dominio
