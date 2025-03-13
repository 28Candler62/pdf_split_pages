from pypdf import PdfReader, PdfWriter

def pdf_split_pages(in_path:str, out_path:str, settings:dict[tuple]):
    
    for infile, out_settings in settings.items():
        o = 0
        pdf_path = f'{in_path}/{infile}'
        outfilename, outpage_numbers = out_settings[o]
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            pdf_writer = PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                while (page_num not in outpage_numbers):
                    o += 1
                    outfilename, outpage_numbers = out_settings[o]
                    pdf_writer = PdfWriter()
                output_filename = f'{out_path}/{outfilename}'                
                pdf_writer.add_page(pdf_reader.pages[page_num])   
                with open(output_filename, "ab") as output_file:
                        pdf_writer.write(output_file)             

if __name__ == "__main__":
    input_path = "infolder"
    output_path = "outfolder"

    output_settings = {
        # "input_file_1.pdf": [
        #     (2, "output_file_1.pdf"),
        #     (3, "output_file_2.pdf"),
        #     (1, "output_file_3.pdf")
        # ],
        # "input_file_2.pdf": [
        #     (10, "other_output_file.pdf"),
        #     (999, "output_file_other.pdf")
        # ],
        # "input_file_3.pdf": [
        #     (15, "names_are_hard.pdf"),
        #     (2, "Im_not_that_creative.pdf"),
        #     (6, "outfile.pdf"),
        #     (2, "ok_Im_done.pdf")
        # ]
    }

    pdf_split_pages(input_path, output_path, output_settings)