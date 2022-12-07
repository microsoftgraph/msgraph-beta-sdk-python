from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

exact_match_session_base = lazy_import('msgraph.generated.models.exact_match_session_base')
exact_match_upload_agent = lazy_import('msgraph.generated.models.exact_match_upload_agent')

class ExactMatchSession(exact_match_session_base.ExactMatchSessionBase):
    @property
    def checksum(self,) -> Optional[str]:
        """
        Gets the checksum property value. The checksum property
        Returns: Optional[str]
        """
        return self._checksum
    
    @checksum.setter
    def checksum(self,value: Optional[str] = None) -> None:
        """
        Sets the checksum property value. The checksum property
        Args:
            value: Value to set for the checksum property.
        """
        self._checksum = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ExactMatchSession and sets the default values.
        """
        super().__init__()
        # The checksum property
        self._checksum: Optional[str] = None
        # The dataUploadURI property
        self._data_upload_u_r_i: Optional[str] = None
        # The fields property
        self._fields: Optional[List[str]] = None
        # The fileName property
        self._file_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The rowsPerBlock property
        self._rows_per_block: Optional[int] = None
        # The salt property
        self._salt: Optional[str] = None
        # The uploadAgent property
        self._upload_agent: Optional[exact_match_upload_agent.ExactMatchUploadAgent] = None
        # The uploadAgentId property
        self._upload_agent_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchSession
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactMatchSession()
    
    @property
    def data_upload_u_r_i(self,) -> Optional[str]:
        """
        Gets the dataUploadURI property value. The dataUploadURI property
        Returns: Optional[str]
        """
        return self._data_upload_u_r_i
    
    @data_upload_u_r_i.setter
    def data_upload_u_r_i(self,value: Optional[str] = None) -> None:
        """
        Sets the dataUploadURI property value. The dataUploadURI property
        Args:
            value: Value to set for the dataUploadURI property.
        """
        self._data_upload_u_r_i = value
    
    @property
    def fields(self,) -> Optional[List[str]]:
        """
        Gets the fields property value. The fields property
        Returns: Optional[List[str]]
        """
        return self._fields
    
    @fields.setter
    def fields(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the fields property value. The fields property
        Args:
            value: Value to set for the fields property.
        """
        self._fields = value
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. The fileName property
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. The fileName property
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
            "checksum": lambda n : setattr(self, 'checksum', n.get_str_value()),
            "data_upload_u_r_i": lambda n : setattr(self, 'data_upload_u_r_i', n.get_str_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_primitive_values(str)),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "rows_per_block": lambda n : setattr(self, 'rows_per_block', n.get_int_value()),
            "salt": lambda n : setattr(self, 'salt', n.get_str_value()),
            "upload_agent": lambda n : setattr(self, 'upload_agent', n.get_object_value(exact_match_upload_agent.ExactMatchUploadAgent)),
            "upload_agent_id": lambda n : setattr(self, 'upload_agent_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def rows_per_block(self,) -> Optional[int]:
        """
        Gets the rowsPerBlock property value. The rowsPerBlock property
        Returns: Optional[int]
        """
        return self._rows_per_block
    
    @rows_per_block.setter
    def rows_per_block(self,value: Optional[int] = None) -> None:
        """
        Sets the rowsPerBlock property value. The rowsPerBlock property
        Args:
            value: Value to set for the rowsPerBlock property.
        """
        self._rows_per_block = value
    
    @property
    def salt(self,) -> Optional[str]:
        """
        Gets the salt property value. The salt property
        Returns: Optional[str]
        """
        return self._salt
    
    @salt.setter
    def salt(self,value: Optional[str] = None) -> None:
        """
        Sets the salt property value. The salt property
        Args:
            value: Value to set for the salt property.
        """
        self._salt = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("checksum", self.checksum)
        writer.write_str_value("dataUploadURI", self.data_upload_u_r_i)
        writer.write_collection_of_primitive_values("fields", self.fields)
        writer.write_str_value("fileName", self.file_name)
        writer.write_int_value("rowsPerBlock", self.rows_per_block)
        writer.write_str_value("salt", self.salt)
        writer.write_object_value("uploadAgent", self.upload_agent)
        writer.write_str_value("uploadAgentId", self.upload_agent_id)
    
    @property
    def upload_agent(self,) -> Optional[exact_match_upload_agent.ExactMatchUploadAgent]:
        """
        Gets the uploadAgent property value. The uploadAgent property
        Returns: Optional[exact_match_upload_agent.ExactMatchUploadAgent]
        """
        return self._upload_agent
    
    @upload_agent.setter
    def upload_agent(self,value: Optional[exact_match_upload_agent.ExactMatchUploadAgent] = None) -> None:
        """
        Sets the uploadAgent property value. The uploadAgent property
        Args:
            value: Value to set for the uploadAgent property.
        """
        self._upload_agent = value
    
    @property
    def upload_agent_id(self,) -> Optional[str]:
        """
        Gets the uploadAgentId property value. The uploadAgentId property
        Returns: Optional[str]
        """
        return self._upload_agent_id
    
    @upload_agent_id.setter
    def upload_agent_id(self,value: Optional[str] = None) -> None:
        """
        Sets the uploadAgentId property value. The uploadAgentId property
        Args:
            value: Value to set for the uploadAgentId property.
        """
        self._upload_agent_id = value
    

