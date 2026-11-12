using ImagesApp.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace ImagesApp_WinF_.Repos
{
    public class FilesRepo
    {
        public List<ImageFile> FilesData { get; set; } = [];
        private List<string> extensions =[];

        public FilesRepo()
        {
            extensions.Add(".jpg");
            extensions.Add(".jpeg");
            extensions.Add(".png");
            extensions.Add(".gif");
            extensions.Add(".bmp");
        }
        public void FillList(string[] pathes)
        {
            foreach (string path in pathes)
            {
                var name = Path.GetFileName(path);
                var ext = Path.GetExtension(path);
                if (extensions.Exists(e => e == ext))
                {
                    var imageFile = new ImageFile()
                    {
                        FilePath = path,
                        FileName = name,
                        FileExt = ext
                    };
                    FilesData.Add(imageFile);
                }
            }
        }
    }
}
