from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

updatable_asset = lazy_import('msgraph.generated.models.windows_updates.updatable_asset')

class UpdateAudiencePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the updateAudience method.
    """
    @property
    def add_exclusions(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the addExclusions property value. The addExclusions property
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._add_exclusions
    
    @add_exclusions.setter
    def add_exclusions(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the addExclusions property value. The addExclusions property
        Args:
            value: Value to set for the addExclusions property.
        """
        self._add_exclusions = value
    
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
    
    @property
    def add_members(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the addMembers property value. The addMembers property
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._add_members
    
    @add_members.setter
    def add_members(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the addMembers property value. The addMembers property
        Args:
            value: Value to set for the addMembers property.
        """
        self._add_members = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new updateAudiencePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The addExclusions property
        self._add_exclusions: Optional[List[updatable_asset.UpdatableAsset]] = None
        # The addMembers property
        self._add_members: Optional[List[updatable_asset.UpdatableAsset]] = None
        # The removeExclusions property
        self._remove_exclusions: Optional[List[updatable_asset.UpdatableAsset]] = None
        # The removeMembers property
        self._remove_members: Optional[List[updatable_asset.UpdatableAsset]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateAudiencePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateAudiencePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateAudiencePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "add_exclusions": lambda n : setattr(self, 'add_exclusions', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
            "add_members": lambda n : setattr(self, 'add_members', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
            "remove_exclusions": lambda n : setattr(self, 'remove_exclusions', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
            "remove_members": lambda n : setattr(self, 'remove_members', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
        }
        return fields
    
    @property
    def remove_exclusions(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the removeExclusions property value. The removeExclusions property
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._remove_exclusions
    
    @remove_exclusions.setter
    def remove_exclusions(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the removeExclusions property value. The removeExclusions property
        Args:
            value: Value to set for the removeExclusions property.
        """
        self._remove_exclusions = value
    
    @property
    def remove_members(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the removeMembers property value. The removeMembers property
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._remove_members
    
    @remove_members.setter
    def remove_members(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the removeMembers property value. The removeMembers property
        Args:
            value: Value to set for the removeMembers property.
        """
        self._remove_members = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("addExclusions", self.add_exclusions)
        writer.write_collection_of_object_values("addMembers", self.add_members)
        writer.write_collection_of_object_values("removeExclusions", self.remove_exclusions)
        writer.write_collection_of_object_values("removeMembers", self.remove_members)
        writer.write_additional_data_value(self.additional_data)
    

