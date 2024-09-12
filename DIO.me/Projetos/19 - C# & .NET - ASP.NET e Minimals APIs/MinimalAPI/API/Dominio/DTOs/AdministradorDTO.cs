using MinimalAPI.API.Dominio.Enums;

namespace MinimalAPI.API.Dominio.DTOs
{
    public class AdministradorDTO
    {
        public string Email { get; set; } = default!;
        public string Senha { get; set; } = default!;
        public Perfil? Perfil { get; set; } = default!;
    }
}