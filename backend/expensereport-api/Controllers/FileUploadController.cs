using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;

namespace expensereport_api.Controllers
{
    [ApiController]
    [Route("/api/[controller]")]
    public class FileUploadController : ControllerBase
    {
        [HttpPost]
        public IActionResult Post()
        {   
            return Ok(JsonConvert.SerializeObject(this.Request.Form.Files));
        }
    }
}