from pypdf import PdfReader, PdfWriter

input_path = "path/to/inputfolder"
output_path = "path/to/outputfolder"

output_settings = {
    "input_file_1.pdf": [
        (2, "output_file_1.pdf"),
        (3, "output_file_2.pdf"),
        (1, "output_file_3.pdf")
    ],
    "input_file_2.pdf": [
        (10, "other_output_file.pdf"),
        (999, "output_file_other.pdf")
    ],
    "input_file_3.pdf": [
        (15, "names_are_hard.pdf"),
        (2, "Im_not_that_creative.pdf"),
        (6, "outfile.pdf"),
        (2, "ok_Im_done.pdf")
    ]
}

def pdf_split_pages(in_path:str, out_path:str, settings:dict[tuple]):
    
    for infile, out_settings in settings.items():
        o = 0
        pdf_path = f'{in_path}\{infile}'
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PdfReader

            for page_num in range(len(pdf_reader.pages)):
                cutoff, outfilename = out_settings[o]
                output_filename = f'{out_path}\{outfilename}'
                page_count = page_num + 1
                pdf_writer = PdfWriter()
                pdf_writer.add_page(pdf_reader.pages[page_num])
                with open(output_filename, "wb") as output_file:
                    pdf_writer.write(output_file)
                if (page_count == cutoff):
                    o += 1