from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel): #se pide crear una clase base para los usuarios
    nombre: str
    apellido: str
    correo: str

class UsuarioCreate(UsuarioBase): 
    clave: str

class UsuarioResponse(UsuarioBase):
    id: int
    class Config:
        orm_mode = True

class AutorBase(BaseModel):
    nombre: str
    apellido: str
    nacionalidad: Optional[str] = None
    fec_nacimiento: Optional[str] = None
    fec_fallecimiento: Optional[str] = None

class AutorCreate(AutorBase): pass
class AutorResponse(AutorBase):
    id: int
    class Config:
        orm_mode = True

class EditorialBase(BaseModel):
    nombre: str

class EditorialCreate(EditorialBase): pass
class EditorialResponse(EditorialBase):
    id: int
    class Config:
        orm_mode = True

class GeneroBase(BaseModel):
    nombre: str

class GeneroCreate(GeneroBase): pass
class GeneroResponse(GeneroBase):
    id: int
    class Config:
        orm_mode = True

class LibroBase(BaseModel):
    titulo: str
    autor_id: int
    editorial_id: int
    genero_id: int
    año_publicacion: Optional[str] = None
    cantidad_disponible: int

class LibroCreate(LibroBase): pass
class LibroResponse(LibroBase):
    id: int
    class Config:
        orm_mode = True

class BibliotecarioBase(BaseModel):
    nombre: str
    apellido: str
    correo: str

class BibliotecarioCreate(BibliotecarioBase):
    clave: str

class BibliotecarioResponse(BibliotecarioBase):
    id: int
    class Config:
        orm_mode = True
