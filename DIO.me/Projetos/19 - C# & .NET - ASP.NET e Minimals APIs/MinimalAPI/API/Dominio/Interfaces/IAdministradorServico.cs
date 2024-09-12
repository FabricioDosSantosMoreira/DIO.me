using MinimalAPI.API.Dominio.DTOs;
using MinimalAPI.API.Dominio.Entidades;

namespace MinimalAPI.API.Dominio.Interfaces
{
    public interface IAdministradorServico
    {
        Administrador? Login(LoginDTO loginDTO);

        Administrador Incluir(Administrador administrador);

        Administrador? BuscaPorId(int id);

        List<Administrador> Todos(int? pagina);
    }
}