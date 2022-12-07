from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CloudPcCrossCloudGovernmentOrganizationMapping(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcCrossCloudGovernmentOrganizationMapping and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The tenant ID in the Azure Government cloud corresponding to the GCC tenant in the public cloud. Currently, 1:1 mappings are supported, so this collection can only contain one tenant ID.
        self._organization_ids_in_u_s_gov_cloud: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcCrossCloudGovernmentOrganizationMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcCrossCloudGovernmentOrganizationMapping
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcCrossCloudGovernmentOrganizationMapping()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "organization_ids_in_u_s_gov_cloud": lambda n : setattr(self, 'organization_ids_in_u_s_gov_cloud', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def organization_ids_in_u_s_gov_cloud(self,) -> Optional[List[str]]:
        """
        Gets the organizationIdsInUSGovCloud property value. The tenant ID in the Azure Government cloud corresponding to the GCC tenant in the public cloud. Currently, 1:1 mappings are supported, so this collection can only contain one tenant ID.
        Returns: Optional[List[str]]
        """
        return self._organization_ids_in_u_s_gov_cloud
    
    @organization_ids_in_u_s_gov_cloud.setter
    def organization_ids_in_u_s_gov_cloud(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the organizationIdsInUSGovCloud property value. The tenant ID in the Azure Government cloud corresponding to the GCC tenant in the public cloud. Currently, 1:1 mappings are supported, so this collection can only contain one tenant ID.
        Args:
            value: Value to set for the organizationIdsInUSGovCloud property.
        """
        self._organization_ids_in_u_s_gov_cloud = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("organizationIdsInUSGovCloud", self.organization_ids_in_u_s_gov_cloud)
    

