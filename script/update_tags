#!/usr/bin/ruby

require 'fileutils'

Dir.mkdir('tag') unless File.directory?('tag')
Dir.foreach "_posts" do |item|
  next if item == "." or item == ".." or File.directory? item
  File.open "_posts/#{item}" do |file|
    str = file.find { |line| line =~ /tags:/ }
    tags = str.gsub(/\s+/m, " ").strip.split(" ")[1..-1]
    tags.each do |tag|
      fname = "tag/#{tag}.html"
      if not File.file? fname
        contents = [
          "---",
          "layout: tag",
          "title: \"Tag: #{tag}\"",
          "tag: #{tag}",
          "---"
        ]
        File.write(fname, contents.join("\n"))
        puts "Created #{fname}"
      else
        puts "#{fname} up-to-date"
      end
    end
  end
end

