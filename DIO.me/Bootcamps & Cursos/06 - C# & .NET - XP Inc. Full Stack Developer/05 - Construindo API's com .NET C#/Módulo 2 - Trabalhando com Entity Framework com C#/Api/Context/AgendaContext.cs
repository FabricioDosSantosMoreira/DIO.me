using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Microsoft.EntityFrameworkCore;

using Api.Entities;

namespace Api.Context
{
    public class AgendaContext : DbContext
    {
        // Recebe as configurações e passa para a classe DbContext
        public AgendaContext(DbContextOptions<AgendaContext> options) : base(options) { }

        // Mapeia uma tabela no BD
        public DbSet<Contato> Contatos{ get; set; }       
    }
}