from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import exact_match_session_base, exact_match_upload_agent

from . import exact_match_session_base

@dataclass
class ExactMatchSession(exact_match_session_base.ExactMatchSessionBase):
    # The checksum property
    checksum: Optional[str] = None
    # The dataUploadURI property
    data_upload_u_r_i: Optional[str] = None
    # The fields property
    fields: Optional[List[str]] = None
    # The fileName property
    file_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The rowsPerBlock property
    rows_per_block: Optional[int] = None
    # The salt property
    salt: Optional[str] = None
    # The uploadAgent property
    upload_agent: Optional[exact_match_upload_agent.ExactMatchUploadAgent] = None
    # The uploadAgentId property
    upload_agent_id: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import exact_match_session_base, exact_match_upload_agent

        fields: Dict[str, Callable[[Any], None]] = {
            "checksum": lambda n : setattr(self, 'checksum', n.get_str_value()),
            "dataUploadURI": lambda n : setattr(self, 'data_upload_u_r_i', n.get_str_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_primitive_values(str)),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "rowsPerBlock": lambda n : setattr(self, 'rows_per_block', n.get_int_value()),
            "salt": lambda n : setattr(self, 'salt', n.get_str_value()),
            "uploadAgent": lambda n : setattr(self, 'upload_agent', n.get_object_value(exact_match_upload_agent.ExactMatchUploadAgent)),
            "uploadAgentId": lambda n : setattr(self, 'upload_agent_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    

