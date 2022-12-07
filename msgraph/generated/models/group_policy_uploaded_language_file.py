from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class GroupPolicyUploadedLanguageFile(AdditionalDataHolder, Parsable):
    """
    The entity represents an ADML (Administrative Template language) XML file uploaded by Administrator.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyUploadedLanguageFile and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The contents of the uploaded ADML file.
        self._content: Optional[bytes] = None
        # The file name of the uploaded ADML file.
        self._file_name: Optional[str] = None
        # Key of the entity.
        self._id: Optional[str] = None
        # The language code of the uploaded ADML file.
        self._language_code: Optional[str] = None
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The contents of the uploaded ADML file.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The contents of the uploaded ADML file.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyUploadedLanguageFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyUploadedLanguageFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyUploadedLanguageFile()
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. The file name of the uploaded ADML file.
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. The file name of the uploaded ADML file.
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "language_code": lambda n : setattr(self, 'language_code', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Key of the entity.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Key of the entity.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def language_code(self,) -> Optional[str]:
        """
        Gets the languageCode property value. The language code of the uploaded ADML file.
        Returns: Optional[str]
        """
        return self._language_code
    
    @language_code.setter
    def language_code(self,value: Optional[str] = None) -> None:
        """
        Sets the languageCode property value. The language code of the uploaded ADML file.
        Args:
            value: Value to set for the languageCode property.
        """
        self._language_code = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("content", self.content)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("languageCode", self.language_code)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

