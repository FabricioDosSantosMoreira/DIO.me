using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using ProjetoAPI.Context;
using ProjetoAPI.Models;

namespace ProjetoAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class TarefaController : ControllerBase
    {
        private readonly DatabaseContext _context;

        public TarefaController(DatabaseContext context)
        {
            _context = context;
        }

        [HttpPost]
        public IActionResult Create(Tarefa tarefa)
        {
            // TODO: Adicionar a tarefa recebida no EF e salvar as mudanças

            if (tarefa.Data == DateTime.MinValue) 
            {
                return BadRequest(new { Erro = "A data da tarefa não pode ser vazia" });
            }

            _context.Add(tarefa);
            _context.SaveChanges();

            return CreatedAtAction(nameof(GetById), new { id = tarefa.Id }, tarefa);
        }

        [HttpGet("GetAll/")]
        public IActionResult GetAll()
        {
            // TODO: Buscar todas as tarefas no banco utilizando o EF

            var tarefasDoBanco = _context.Tarefas.ToList();
            if (tarefasDoBanco.Count == 0) 
            {
                return NotFound($"Nenhuma tarefa encontrada!");
            }

            return Ok(tarefasDoBanco);
        }

        [HttpGet("GetById/{id}")]
        public IActionResult GetById(int id)
        {   
            // TODO: Buscar o Id no banco utilizando o EF
            // TODO: Validar o tipo de retorno. Se não encontrar a tarefa, retornar NotFound,
            // caso contrário retornar OK com a tarefa encontrada

            var tarefaDoBanco = _context.Tarefas.Find(id);
            if (tarefaDoBanco == null) 
            {
                return NotFound($"Tarefa com Id={id} não encontrada!");
            }
        
            return Ok(tarefaDoBanco);
        }
        
        [HttpGet("GetByTitulo/")]
        public IActionResult GetByTitulo(string titulo)
        {
            // TODO: Buscar  as tarefas no banco utilizando o EF, que contenha o titulo recebido por parâmetro

            var tarefaDoBanco = _context.Tarefas.Where( x => x.Titulo.Contains(titulo));
            if (!tarefaDoBanco.Any()) 
            {
                return NotFound($"Tarefa com Titulo={titulo} não encontrada!");
            }

            return Ok(tarefaDoBanco);
        }

        [HttpGet("GetByData/")]
        public IActionResult GetByData(DateTime data)
        {
            var tarefaDoBanco = _context.Tarefas.Where(x => x.Data.Date == data.Date);
            if (!tarefaDoBanco.Any()) 
            {
                return NotFound($"Tarefa com Data={data} não encontrada!");
            }

            return Ok(tarefaDoBanco);
        }

        [HttpGet("GetByStatus/")]
        public IActionResult GetByStatus(EnumStatusTarefa status)
        {
            // TODO: Buscar  as tarefas no banco utilizando o EF, que contenha o status recebido por parâmetro
            var tarefaDoBanco = _context.Tarefas.Where(x => x.Status == status);
            if (!tarefaDoBanco.Any()) 
            {
                return NotFound($"Tarefa com Status={status} não encontrada!");
            }

            return Ok(tarefaDoBanco);
        }

        [HttpPut("UpdateById/{id}")]
        public IActionResult UpdateById(int id, Tarefa tarefa)
        {
            // TODO: Atualizar as informações da variável tarefaBanco com a tarefa recebida via parâmetro
            // TODO: Atualizar a variável tarefaBanco no EF e salvar as mudanças

            var tarefaDoBanco = _context.Tarefas.Find(id);
            if (tarefaDoBanco == null) 
            {
                return NotFound($"Tarefa com Id={id} inexistente!");
            }

            if (tarefa.Data == DateTime.MinValue) 
            {
                return BadRequest(new { Erro = "A data da tarefa não pode ser vazia" });
            }

            tarefaDoBanco.Titulo = tarefa.Titulo;
            tarefaDoBanco.Descricao = tarefa.Descricao;
            tarefaDoBanco.Data = tarefa.Data;
            tarefaDoBanco.Status = tarefa.Status;
            
            _context.Tarefas.Update(tarefaDoBanco);
            _context.SaveChanges();

            return Ok(tarefaDoBanco);
        }

        [HttpDelete("DeleteById/{id}")]
        public IActionResult DeleteById(int id)
        {   
            // TODO: Remover a tarefa encontrada através do EF e salvar as mudanças

            var tarefaDoBanco = _context.Tarefas.Find(id);
            if (tarefaDoBanco == null) 
            {
                return NotFound($"Tarefa com Id={id} inexistente!");
            }

            _context.Tarefas.Remove(tarefaDoBanco);
            _context.SaveChanges();

            return NoContent();
        }
    }
}
