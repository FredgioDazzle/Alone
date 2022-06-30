init -1 python:

    def define_bg(bg_name="", format_im="", variants=True, bg_scale=1.0):
            
        bg_dir = "/bg/"

        variants_list = []
        with renpy.file("images" + bg_dir + "bg_variants_list.los") as bg_file:
            for line in bg_file:
                list_1 = line.split(",")
                list_2 = []
                for x in range(len(list_1)):
                    list_3 = str(list_1)
                    list_2.append(list_3)

        if bg_name == "":
            renpy.error(_("Se necesita un nombre para el BG."))

        if format_im == "":
            renpy.error(_("El formato de la imagen BG es necesario."))

        if variants == True:
            for var in variants_list:
                
                renpy.image(bg_name + variants_list[var] + "_blur", im.Blur(bg_dir + bg_name + variants_list[var] + format_im, persistent.blur_default)) 
                renpy.image(bg_name + variants_list[var], bg_dir + bg_name + variants_list[var] + format_im)

                if renpy.exists(bg_dir + bg_name + variants_list[var] + "_front" + format_im):
                    renpy.image(bg_name + variants_list[var] + "_blur"+ "_front", im.Blur(bg_dir + bg_name + variants_list[var] + "_front" + format_im, persistent.blur_default)) 
                    renpy.image(bg_name + variants_list[var]+ "_front", bg_dir + bg_name + variants_list[var] + "_front" + format_im)
                elif bg_scale:
                    renpy.image(bg_name + variants_list[var] + "_blur"+ "_front", im.FactorScale(im.Blur(bg_dir + bg_name + variants_list[var] + "_front" + format_im, persistent.blur_default), bg_scale))
                    renpy.image(bg_name + variants_list[var] + "_front", im.FactorScale(bg_dir + bg_name + variants_list[var] + "_front" + format_im, bg_scale))

        else:
            renpy.image(bg_name + "_blur", im.Blur(bg_dir + bg_name + format_im, persistent.blur_default))# playerroom_blur
            renpy.image(bg_name, bg_dir + bg_name + format_im, )# playerroom

            if renpy.exists(bg_dir + bg_name  + "_front" + format_im):
                renpy.image(bg_name + "_front" + "_blur", im.Blur(bg_dir + bg_name + "_front" + format_im, persistent.blur_default)) 
                renpy.image(bg_name + "_front", bg_dir + bg_name + "_front" + format_im)
            elif bg_scale > 1.0 and not renpy.exists(bg_dir + bg_name  + "_front" + format_im):
                renpy.image(bg_name + "_front" + "_blur", im.FactorScale(im.Blur(bg_dir + bg_name + format_im, persistent.blur_default), bg_scale))
                renpy.image(bg_name + "_front", im.FactorScale(bg_dir + bg_name + format_im, bg_scale))

    define_bg("hiroki_room", ".jpg", True)
    define_bg("hiroki_livingroom", ".jpg",  None)
    define_bg("apartment_exterior", ".jpg", None)
    define_bg("schoolen", ".jpg", None)
    define_bg("classroom", ".jpg", None)
    define_bg("city1", ".jpg", None)
    define_bg("city2", ".jpg", None)
    define_bg("yumi_door", ".jpg", None)
    define_bg("yumi_livingroom", ".jpg", True)
    define_bg("yumi_kitchen", ".jpg", True)
    define_bg("yumi_hall", ".jpg", True)
    define_bg("yumi_bathroom", ".jpg", True)
    define_bg("yumi_room", ".jpg", True)
    define_bg("isseihouse", ".jpg", None, 1.8)
    define_bg("issei_livingroom", ".jpg", None)