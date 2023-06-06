from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AppIdentity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Refers to the unique identifier representing Application Id in the Azure Active Directory.
    app_id: Optional[str] = None
    # Refers to the Application Name displayed in the Azure Portal.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Refers to the unique identifier indicating Service Principal Id in Azure Active Directory for the corresponding App.
    service_principal_id: Optional[str] = None
    # Refers to the Service Principal Name is the Application name in the tenant.
    service_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
            "servicePrincipalName": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

