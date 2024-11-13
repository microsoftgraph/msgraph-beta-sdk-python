from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_format import ApiFormat
    from .credential import Credential
    from .industry_data_connector import IndustryDataConnector
    from .one_roster_api_data_connector import OneRosterApiDataConnector

from .industry_data_connector import IndustryDataConnector

@dataclass
class ApiDataConnector(IndustryDataConnector, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.apiDataConnector"
    # The apiFormat property
    api_format: Optional[ApiFormat] = None
    # The base URL, including the scheme, host, and path for the API, with or without a trailing '/'. For example, 'https://example.com/ims/oneRoster/v1p1'
    base_url: Optional[str] = None
    # The credential property
    credential: Optional[Credential] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApiDataConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApiDataConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.oneRosterApiDataConnector".casefold():
            from .one_roster_api_data_connector import OneRosterApiDataConnector

            return OneRosterApiDataConnector()
        return ApiDataConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .api_format import ApiFormat
        from .credential import Credential
        from .industry_data_connector import IndustryDataConnector
        from .one_roster_api_data_connector import OneRosterApiDataConnector

        from .api_format import ApiFormat
        from .credential import Credential
        from .industry_data_connector import IndustryDataConnector
        from .one_roster_api_data_connector import OneRosterApiDataConnector

        fields: Dict[str, Callable[[Any], None]] = {
            "apiFormat": lambda n : setattr(self, 'api_format', n.get_enum_value(ApiFormat)),
            "baseUrl": lambda n : setattr(self, 'base_url', n.get_str_value()),
            "credential": lambda n : setattr(self, 'credential', n.get_object_value(Credential)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .api_format import ApiFormat
        from .credential import Credential
        from .industry_data_connector import IndustryDataConnector
        from .one_roster_api_data_connector import OneRosterApiDataConnector

        writer.write_enum_value("apiFormat", self.api_format)
        writer.write_str_value("baseUrl", self.base_url)
        writer.write_object_value("credential", self.credential)
    

