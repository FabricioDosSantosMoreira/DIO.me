using Microsoft.EntityFrameworkCore;

using ProjetoAPI.Models;

namespace ProjetoAPI.Context
{
    public class DatabaseContext : DbContext
    {
        public DatabaseContext(DbContextOptions<DatabaseContext> options) : base(options) { }

        public DbSet<Tarefa> Tarefas { get; set; }
    }
}