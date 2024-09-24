using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Microsoft.AspNetCore.Mvc;

using Api.Entities;
using Api.Context;

namespace Api.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ContatoController : ControllerBase
    {
        private readonly AgendaContext _context;

        public ContatoController(AgendaContext context)
        {
            _context = context;
        }

        [HttpPost]
        public IActionResult Create(Contato contato)
        {
            _context.Add(contato);
            _context.SaveChanges();

            return CreatedAtAction(nameof(GetById), new { id = contato.Id }, contato);
        }

        [HttpGet("GetById/{id}")]
        public IActionResult GetById(long id)
        {
            var contatoDoBanco = _context.Contatos.Find(id);
            if (contatoDoBanco == null) 
            {
                return NotFound($"Contato com Id={id} não encontrado!");
            }

            return Ok(contatoDoBanco);
        }

        [HttpGet("GetByNome")]
        public IActionResult GetByNome(string nome) 
        {
            var contatosDoBanco = _context.Contatos.Where(x => x.Nome.Contains(nome));
            if (!contatosDoBanco.Any()) 
            {
                return NotFound($"Contato com Nome={nome} não encontrado!");
            }

            return Ok(contatosDoBanco);
        }

        [HttpGet("GetAll")]
        public IActionResult GetAll()
        {
            var contatosDoBanco = _context.Contatos.ToList();
            if (contatosDoBanco.Count == 0) 
            {
                return NotFound($"Nenhum contato encontrado!");
            }

            return Ok(contatosDoBanco);
        }

        [HttpPut("UpdateById/{id}")]
        public IActionResult UpdateById(long id, Contato contato)
        {
            var contatoDoBanco = _context.Contatos.Find(id);
            if (contatoDoBanco == null) 
            {
                return NotFound($"Contato com Id={id} inexistente!");
            }

            // Se a chave "ativo" do json vier com valor bool aceita ela
            // Ver em Entities/Contato 'bool? Ativo'
            if (contato.Ativo.HasValue)
            {
                contatoDoBanco.Ativo = contato.Ativo.Value;
            }

            if (contato.Nome != null) 
            {
                contatoDoBanco.Nome = contato.Nome;
            }
        
            if (contato.Telefone != null) 
            {
                contatoDoBanco.Telefone = contato.Telefone;
            }
            
            _context.Contatos.Update(contatoDoBanco);
            _context.SaveChanges();

            return Ok(contatoDoBanco);
        }

        [HttpDelete("DeleteById/{id}")]
        public IActionResult DeleteById(long id)
        {
            var contatoDoBanco = _context.Contatos.Find(id);
            if (contatoDoBanco == null) 
            {
                return NotFound($"Contato com Id={id} inexistente!");
            }

            _context.Contatos.Remove(contatoDoBanco);
            _context.SaveChanges();

            return NoContent();
        }
    }
}