from string import Template

tpl_start_text = """
    .text
main: 
"""

tpl_start_data = """
    .data
"""

tpl_var_decl = Template("""
$varname: .word 0
""")

tpl_end = """
    li	    $v0     10                  
    syscall
"""

tpl_immediate = Template("""
    li      $$a0    $immediate
""")

tpl_suma = Template("""
$left
    sw      $$a0    0($$sp)             
    addiu   $$sp    $$sp        -4
$right
    lw      $$t1    4($$sp)             
    addiu   $$sp    $$sp        4       
    add     $$a0    $$a0        $$t1
""")

tpl_print_int = Template("""
$prev
	li	    $$v0     1              
	syscall			                
""")

tpl_var = Template("""
    lw      $$a0        $name
""")

tpl_asignacion = Template("""
$prev
    sw      $$a0        $name       
""")

"""
	i: .word 0
    

	li 	$v0, 5  			
	syscall					
    move	$t0,$v0         

   

.data
msg: .asciiz “\nHello, World!\n”

li $v0, 4
la $a0, msg
syscall
"""