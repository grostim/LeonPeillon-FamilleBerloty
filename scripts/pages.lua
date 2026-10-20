-- Conserve les repères photographiques dans la source LaTeX sans les imprimer.
function RawBlock(el)
  if el.format == 'html' and el.text:match('^<!%-%-') then
    return pandoc.RawBlock('latex', '% ' .. el.text:gsub('^<!%-%-%s*', ''):gsub('%s*%-%->$', ''))
  end
end
